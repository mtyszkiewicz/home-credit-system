<script>
  import "../app.css";
  export let data;
</script>

{#if data?.user?.id}
  <nav class="flex sm:justify-center space-x-4">
    <a
      href="/?user_id={data?.user.id}"
      class="rounded-lg px-3 py-2 text-slate-700 font-medium hover:bg-slate-100 hover:text-slate-900"
      >Profile</a
    >
    <a
      href="/summary?user_id={data?.user.id}"
      class="rounded-lg px-3 py-2 text-slate-700 font-medium hover:bg-slate-100 hover:text-slate-900"
      >Summary</a
    >
    <a
      href="/history?user_id={data?.user.id}"
      class="rounded-lg px-3 py-2 text-slate-700 font-medium hover:bg-slate-100 hover:text-slate-900"
      >History</a
    >
  </nav>
  <slot />
{:else}
<main
  class="relative flex flex-col items-center justify-center min-h-screen py-10 overflow-hidden"
>
  <h1 class="text-red-600 text-5xl font-bold text-center">
    UNKNOWN IDENTITY
  </h1>
</main>

{/if}
