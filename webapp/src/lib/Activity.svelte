<!-- Activity.svelte -->
<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import type { Activity } from "../types";
  export let activity: Activity;

  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch("activityClick", activity.id);
  }
</script>

<div class="flex items-center space-x-4">
  <div class="space-x-1">
    <span class="text-xl">{activity.icon}</span>
    <span class="font-sm leading-none">{activity.name}</span>
    <button
      class={`justify-self-end px-2 py-1 rounded shadow transition-colors duration-200 ${
        activity.value > 0 ? "bg-green-500 text-white" : "bg-red-500 text-white"
      }`}
      on:click={handleClick}
    >
      {#if activity.value > 0}
        +{activity.value}
      {:else}
        {activity.value}
      {/if}
    </button>
  </div>
</div>

<style>
  .bg-green-500:hover {
    background-color: #047857;
  }
  .bg-red-500:hover {
    background-color: #9f3a38;
  }
</style>
