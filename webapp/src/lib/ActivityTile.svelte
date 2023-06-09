<script lang="ts">
  import type { Activity } from "../types";
  import { onMount } from "svelte";

  let dialog: HTMLDialogElement;
  onMount(() => {
    dialog = document.getElementById(`activity-dialog-${activity.id}`)!;
  });

  export let activity: Activity;
</script>

<button
  class="py-4 m-2 dark:bg-zinc-800 dark:hover:bg-zinc-700 bg-zinc-100 rounded-lg shadow-md text-center text-3xl"
  on:click={() => dialog.showModal()}
>
  {activity.icon}
</button>
