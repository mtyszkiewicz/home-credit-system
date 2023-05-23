import type { User } from "../types";


export async function load({ url }) {
  const API_BASE: string = `http://${url.hostname}:5055`;
  const userId = url.searchParams.get("user_id");

  if (userId === null) {
    return {};
  }

  const userRes = await fetch(`${API_BASE}/users/${userId}`);
  const user: User = await userRes.json();

  return {
    user: user,
  };
}
