<script>
  export let data; // History
</script>

<main class="min-h-screen py-4">
  <div
  class="w-full max-w-xl p-6 mb-6 mx-auto rounded-lg shadow-xl dark:bg-white/10 bg-white/30 ring-1 ring-gray-900/5 backdrop-blur-lg"
>
    {#each data.history as day}
      <p class="text-xl mt-4">{day.date}</p>
      {#each day.records as record (record.id)}
        <div class="py-2 pl-4 divide-y divide-gray-900/5">
            <div class="space-x-1">
              <span class="text-sm text-gray-600">{record.time}</span>
              <span class="font-sm bg-{record.user.color}-500 p-1 bg-opacity-40 rounded-lg">{record.user.name}</span>
              <span class="font-sm">{record.activity.icon}</span>
              <span class="font-sm">{record.activity.name}</span>
            </div>
        </div>
      {/each}
    {/each}
    </div>
</main>