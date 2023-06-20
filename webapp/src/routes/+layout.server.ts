import type { User } from "../types";


export async function load({ url }) {
  const API_BASE: string = `http://${url.hostname}:5055`;
  const accessToken = url.searchParams.get("access_token");

  if (accessToken === null) {
    return {};
  }

  const authResponse = await fetch(`${API_BASE}/auth?access_token=${accessToken}`);
  const user: User = await authResponse.json();

  return {
    user: user,
    accessToken: accessToken
  };
}
