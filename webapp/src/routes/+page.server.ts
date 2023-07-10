import type { Activity, User } from "../types";



export async function load({ url }) {
  const API_BASE: string = `http://${url.hostname}:5055`;
  const activitiesRes = await fetch(`${API_BASE}/activities`);
  const activities: Activity[] = await activitiesRes.json();
  return {
    activities: activities
  };
}
