// Takes a relative path that is passed to it and
// appends it to the base URL of the website.
export const getImageUrl = (path) => {
  return new URL(`/assets/${path}}`, import.meta.url).href;
};
