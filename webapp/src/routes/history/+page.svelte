<script>
    export let data;
</script>

<main
  class="relative flex flex-col items-center justify-center min-h-screen py-10"
>
    <div
      class="w-full max-w-xl p-12 mx-auto rounded-lg shadow-xl dark:bg-white/10 bg-white/30 ring-1 ring-gray-900/5 backdrop-blur-lg"
    >
      <div class="divide-y divide-gray-900/5">
        {#each data.history as day}
          <p class="text-xl">{day.date}</p>
            {#each day.records as record (record.id)}
              <div class="flex items-center py-2 place-content-start pl-8">
                  <div class="flex items-center space-x-4">
                    <div class="space-x-1">
                      <span class="text-sm">{record.time}</span>
                      <span class="font-sm leading-none">{record.user.name}</span>
                      <span class="font-sm leading-none">{record.activity.icon}</span>
                      <span class="font-sm leading-none">{record.activity.name}</span>
                    </div>
                  </div>
              </div>
            {/each}
        {/each}
      </div>
    </div>
</main>