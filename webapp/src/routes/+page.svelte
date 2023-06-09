<script lang="ts">
  import UserProfile from "../lib/UserProfile.svelte";
  import ActivityTile from "../lib/ActivityTile.svelte";
  import ActivityDialog from "../lib/ActivityDialog.svelte";
  import type { Activity } from "../types";
  import { page } from "$app/stores";
  const API_BASE = `http://${$page.url.hostname}:5055`;
  export let data;
  $: score = data.user.score;

  async function handleActivitySubmit(
    event: CustomEvent<{ activity: Activity }>
  ) {
    await fetch(
      `${API_BASE}/users/${data.user.id}/activity_records?activity_id=${event.detail.activity.id}`,
      { method: "POST" }
    );
    score += event.detail.activity.value;
  }
</script>

<div
  class="p-6 w-96 rounded-lg shadow-xl dark:bg-white/10 bg-white/30 ring-1 ring-gray-900/5 backdrop-blur-lg"
>
  <div class="flex place-content-around pb-4">
    <UserProfile user={data.user} {score} />
  </div>

  <div class="grid grid-cols-4">
    {#each data.activities as activity (activity.id)}
      <ActivityDialog {activity} on:submit={handleActivitySubmit} />
      <ActivityTile {activity} />
    {/each}
  </div>
</div>
