<script>
  export let data; // History
</script>

<main class="min-h-screen">
  <div
    class="pl-6 pt-6 w-96 space-y-2 rounded-lg shadow-xl dark:bg-white/10 bg-white/30 ring-1 ring-gray-900/5 backdrop-blur-lg"
  >
    {#each data.history as day}
      <p class="text-xl">{day.date}</p>
      <div class="grid grid-cols-7 pl-2 items-center gap-y-2">
      {#each day.records as record (record.id)}
          <span class="text-sm text-gray-500 text-center w-10">{record.time}</span>
          <span
            class="font-sm text-center w-16 bg-{record.user.color}-500 bg-opacity-35 rounded-md">{record.user.name}</span>
          <span class="font-sm px-5">{record.activity.icon}</span>
          <div class="font-sm col-span-4 ml">{record.activity.name}</div>
      {/each}
      <div></div>
    </div>
    {/each}
  </div>
</main>
