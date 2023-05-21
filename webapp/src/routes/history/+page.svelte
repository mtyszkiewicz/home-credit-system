<script>
  export let data; // History
</script>

<main class="min-h-screen py-4">
  <div
    class="w-full max-w-xl p-6 mb-6 mx-auto rounded-lg shadow-xl dark:bg-white/10 bg-white/30 ring-1 ring-gray-900/5 backdrop-blur-lg"
  >
    {#each data.history as day}
      <p class="text-xl mt-4">{day.date}</p>
      <div class="grid grid-cols-7 place-items-baseline space-y-2 pl-2">
      {#each day.records as record (record.id)}
          <span class="text-sm text-gray-600">{record.time}</span>
          <span
            class="font-sm place-self-center bg-{record.user.color}-500 px-1 bg-opacity-35 rounded-md">{record.user.name}</span>
          <span class="font-sm place-self-end px-2">{record.activity.icon}</span>
          <div class="font-sm col-span-4">{record.activity.name}</div>
      {/each}
    </div>
    {/each}
  </div>
</main>
