import React from 'react';
import { StyleSheet, StatusBar, Platform } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { WebView } from 'react-native-webview';

const URL = process.env.EXPO_PUBLIC_API_URL || 'https://ghost993-expensemanager.hf.space';

const injectScripts = `
  // Fix for mobile viewport scaling
  var meta = document.createElement('meta');
  meta.name = 'viewport';
  meta.content = 'width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no';
  document.getElementsByTagName('head')[0].appendChild(meta);

  // Fix for Google Sign-In redirect bug in webapp's google-auth.js
  const originalFetch = window.fetch;
  window.fetch = function() {
    return originalFetch.apply(this, arguments).then(res => {
      if (arguments[0] === '/api/auth/google' || arguments[0].includes('/api/auth/google')) {
        if (res.ok) {
          const originalJson = res.json.bind(res);
          res.json = async function() {
            const data = await originalJson();
            data.redirect = '/dashboard'; // Force redirect to dashboard
            return data;
          };
        }
      }
      return res;
    });
  };
  true;
`;

export default function App() {
  const webviewRef = React.useRef(null);

  const onNavigationStateChange = (navState) => {
    // If the Flask backend redirects to /login (which 404s), force it to the root URL
    if (navState.url.endsWith('/login') && navState.url.includes('hf.space')) {
      webviewRef.current?.stopLoading();
      webviewRef.current?.injectJavaScript(`window.location.href = '${URL}'; true;`);
    }
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="light-content" backgroundColor="#121212" />
      <WebView 
        ref={webviewRef}
        source={{ 
          uri: URL,
          headers: { 'X-Requested-With': '' } 
        }} 
        style={styles.webview}
        javaScriptEnabled={true}
        domStorageEnabled={true}
        startInLoadingState={true}
        originWhitelist={['*']}
        userAgent="Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
        thirdPartyCookiesEnabled={true}
        sharedCookiesEnabled={true}
        setSupportMultipleWindows={false}
        onNavigationStateChange={onNavigationStateChange}
        injectedJavaScript={injectScripts}
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#121212',
    paddingTop: Platform.OS === 'android' ? StatusBar.currentHeight : 0
  },
  webview: {
    flex: 1,
    backgroundColor: '#121212'
  }
});
