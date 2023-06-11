<script lang="ts">
  import type { Activity } from "../types";
  import { createEventDispatcher } from "svelte";

  const dispatch = createEventDispatcher();

  function submitActivity() {
    dispatch("submit", {
      activity: activity,
    });
  }

  export let activity: Activity;
</script>

<dialog
  id="activity-dialog"
  class="w-80 backdrop:bg-zinc-800 backdrop:bg-opacity-50 dark:bg-zinc-900 rounded-lg dialog-scale"
>
  <form method="dialog">
    <div class="flex items-center">
      <span class="text-4xl self-start m-2">{activity.icon}</span>
      <span class="text-xl dark:text-zinc-300 text-zinc-600 mr-1"
        >{activity.name}</span
      >
      <span class={`${activity.value > 0 ? "text-green-500" : "text-red-500"}`}>
        {activity.value > 0 ? "+" : ""}{activity.value}
      </span>
    </div>
    {#if activity.requirements.length > 0}
    <ul class="dark:text-zinc-300 text-zinc-600 text-sm p-2">
      {#each activity.requirements as req}
        <li>‣ {req}</li>
      {/each}
    </ul>
    {/if}

    <div class="flex items-center justify-center gap-x-4 text-xl m-4">
      <button
        type="submit"
        class="px-2 py-1 dark:bg-red-600 bg-red-500 rounded text-red-200"
        >Cancel</button
      >
      <button
        type="submit"
        on:click={() => submitActivity()}
        class="px-2 py-1 dark:bg-green-600 bg-green-500 text-green-200 rounded"
        >Submit</button
      >
    </div>
  </form>
</dialog>

<style>
  @keyframes scaleUp {
    from {
      transform: scale(0);
    }
    to {
      transform: scale(1);
    }
  }

  .dialog-scale {
    animation: scaleUp 0.2s ease-in-out;
  }
</style>
