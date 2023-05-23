import type { User } from "../types";

const API_BASE: string = `http://${$page.url.hostname}:5055`;

export async function load({ url }) {
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
