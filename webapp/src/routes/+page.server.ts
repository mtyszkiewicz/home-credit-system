import type { Activity, User } from "../types";
import { env } from '$env/dynamic/private'



export async function load({ url }) {
  const activitiesRes = await fetch(`${env.API_BASE_URL}/activities`);
  const activities: Activity[] = await activitiesRes.json();
  return {
    activities: activities
  };
}
