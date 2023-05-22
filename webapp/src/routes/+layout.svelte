<script>
  import { page } from '$app/stores'
  import "../app.css";
  export let data;
</script>

{#if data?.user?.id}
  <nav class="flex justify-center py-2 space-x-2">
    <a
      href="/?user_id={data?.user.id}"
      class="lg:hover:bg-slate-100 lg:hover:text-slate-900 lg:hover:border-1 lg:hover:bg-opacity-50"
      class:active={$page.url.pathname === '/'}
      >Profile</a
    >
    <a
      href="/summary?user_id={data?.user.id}"
      class="lg:hover:bg-slate-100 lg:hover:text-slate-900 lg:hover:border-1 lg:hover:bg-opacity-50"
      class:active={$page.url.pathname === '/summary'}
      >Summary</a
    >
    <a
      href="/history?user_id={data?.user.id}"
      class="lg:hover:bg-slate-100 lg:hover:text-slate-900 lg:hover:border-1 lg:hover:bg-opacity-50"
      class:active={$page.url.pathname === '/history'}
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
    <p class ="text-9xl">🤡</p>
  </main>
{/if}
<style>
  .active {
    @apply bg-slate-100 text-slate-950 transition-shadow duration-200 shadow-md;
  }
  a {
    @apply rounded-lg py-2 font-medium text-gray-500 w-24 text-center touch-none;
  }
</style>
