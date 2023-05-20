<script>
  import "../app.css";
  export let data;
</script>

{#if data?.user?.id}
  <nav class="flex justify-center py-2 space-x-2">
    <a
      href="/?user_id={data?.user.id}"
      class="rounded-lg py-2 font-medium text-slate-700 hover:bg-slate-100 hover:text-slate-900 hover:border-1 w-24 text-center"
      >Profile</a
    >
    <a
      href="/summary?user_id={data?.user.id}"
      class="rounded-lg py-2 font-medium text-slate-700 hover:bg-slate-100 hover:text-slate-900 hover:border-1 w-24 text-center"
      >Summary</a
    >
    <a
      href="/history?user_id={data?.user.id}"
      class="rounded-lg py-2 font-medium text-slate-700 hover:bg-slate-100 hover:text-slate-900 hover:border-1 w-24 text-center"
      >History</a
    >
  </nav>
  <main class="flex flex-col items-center min-h-screen py-4">
    <slot />
  </main>
{:else}
  <main
    class="relative flex flex-col items-center justify-center min-h-screen py-10 overflow-hidden"
  >
    <h1 class="text-red-600 text-5xl font-bold text-center">
      UNKNOWN IDENTITY
    </h1>
  </main>
{/if}
