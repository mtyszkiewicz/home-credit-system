import { env } from "$env/dynamic/private";
import type { User } from "../types";


export async function load({ url }) {
  const accessToken = url.searchParams.get("access_token");

  if (accessToken === null) {
    return {};
  }

  const authResponse = await fetch(`${env.API_BASE_URL}/auth?access_token=${accessToken}`);
  const user: User = await authResponse.json();

  return {
    user: user,
    accessToken: accessToken
  };
}
