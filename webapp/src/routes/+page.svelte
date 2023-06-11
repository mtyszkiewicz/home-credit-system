<script lang="ts">
  import UserProfile from "../lib/UserProfile.svelte";
  import ActivityDialog from "../lib/ActivityDialog.svelte";
  import { onMount } from "svelte";
  import type { Activity } from "../types";
  import { page } from "$app/stores";
  const API_BASE = `http://${$page.url.hostname}:5055`;
  export let data;
  $: score = data.user.score;
  $: selectedActivity = data.activities[0];

  let dialog: HTMLDialogElement;
  onMount(() => {
    dialog = document.getElementById("activity-dialog")!;
  });

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

  <div class="grid grid-cols-3">
    <ActivityDialog activity={selectedActivity} on:submit={handleActivitySubmit} />
    {#each data.activities as activity (activity.id)}
      <button
        class="py-4 m-2 dark:bg-zinc-800 dark:hover:bg-zinc-700 bg-zinc-100 rounded-lg shadow-md"
        on:click={() => {selectedActivity = activity; dialog.showModal()}}
      >
      <span class="text-center text-3xl">{activity.icon}</span>
        <div class="text-xs mx-1">
          {activity.name}
        </div>
      </button>
    {/each}
  </div>
</div>
