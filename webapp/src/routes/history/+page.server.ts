
const API_BASE: string = "http://192.168.1.17:5055";

export async function load() {
  const history = fetch(`${API_BASE}/activity_records`).then(res => res.json());

  return {
    history: history
  }
}