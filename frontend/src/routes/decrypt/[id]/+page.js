export async function load({ params, url }) {
    return {
      id: params.id,
      key: url.searchParams.get("key"),
      iv: url.searchParams.get("iv"),
    };
  }