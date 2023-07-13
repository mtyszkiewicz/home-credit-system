import { env } from '$env/dynamic/private';
import type { ActivityRecordsHistory } from '../../types';

export async function load({ url }) {
  const historyRes = await fetch(`${env.API_BASE_URL}/activity_records`);
  const history: ActivityRecordsHistory[] = await historyRes.json();

  return {
    history: history
  }
}
