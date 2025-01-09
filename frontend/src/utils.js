/**
 * Copies text to clipboard
 * @param {string} text - The text to copy
 * @returns {Promise<void>}
 */
export const copyToClipboard = async text => {
  try {
    await navigator.clipboard.writeText(text);
    return Promise.resolve();
  } catch (err) {
    console.error('Failed to copy: ', err);
    return Promise.reject(err);
  }
};

/**
 * Converts base64 string to URL safe format
 * @param {string} base64String - The base64 string to convert
 * @returns {string} URL safe base64 string
 */
export const toBase64UrlSafe = base64String => {
  return base64String.replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, '');
};
