<script lang="ts">
  import { page } from '$app/stores';
  import ThemeSelector from './ThemeSelector.svelte';
  import { isLoggedIn } from '$lib/stores/stores';

  function animateSVG(event: MouseEvent): void {
    let path = (event.currentTarget as HTMLElement).querySelector('path');
    let length = path?.getTotalLength() || 0;
    if (path) {
      // Reset styles to initial state
      path.style.strokeDasharray = length.toString();
      path.style.strokeDashoffset = length.toString();
      path.style.transition = 'none'; // Remove transition temporarily

      // Forces a repaint to make sure the styles are applied
      path.getBoundingClientRect();

      // Apply the animation
      path.style.transition = 'stroke-dashoffset 2s ease-in-out';
      path.style.strokeDashoffset = '0';
    }
  }
</script>

<div class="page-fade-in">
  <div
    class="navbar rounded-b mb-2 bg-gradient-to-b from-primary to-transparent text-neutral-content max-h-20"
    id="navbar"
  >
    <div class="flex-none sm:px-2 sm:mx-2">
      <ul
        class="menu menu-horizontal shadow-lg bg-gradient-to-b from-primary to-transparent rounded-box"
      >
        {#if !$isLoggedIn}
          <li>
            <a
              href="/"
              aria-label="home"
              title="Home"
              class={$page.url.pathname === '/home' ? 'rounded bg-white' : ''}
              on:click={animateSVG}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="stroke-current {$page.url.pathname === '/home'
                  ? 'text-primary'
                  : 'text-white'} h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" /></svg
              ></a
            >
          </li>
        {:else}
          <li>
            <a
              href="smart-goals"
              aria-label="smart goals"
              title=" Smart Goals"
              class={$page.url.pathname === '/smart-goals' ? 'rounded bg-white' : ''}
              on:click={animateSVG}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="stroke-current {$page.url.pathname === '/smart-goals'
                  ? 'text-primary'
                  : 'text-white'} h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M16.5 18.75h-9m9 0a3 3 0 013 3h-15a3 3 0 013-3m9 0v-3.375c0-.621-.503-1.125-1.125-1.125h-.871M7.5 18.75v-3.375c0-.621.504-1.125 1.125-1.125h.872m5.007 0H9.497m5.007 0a7.454 7.454 0 01-.982-3.172M9.497 14.25a7.454 7.454 0 00.981-3.172M5.25 4.236c-.982.143-1.954.317-2.916.52A6.003 6.003 0 007.73 9.728M5.25 4.236V4.5c0 2.108.966 3.99 2.48 5.228M5.25 4.236V2.721C7.456 2.41 9.71 2.25 12 2.25c2.291 0 4.545.16 6.75.47v1.516M7.73 9.728a6.726 6.726 0 002.748 1.35m8.272-6.842V4.5c0 2.108-.966 3.99-2.48 5.228m2.48-5.492a46.32 46.32 0 012.916.52 6.003 6.003 0 01-5.395 4.972m0 0a6.726 6.726 0 01-2.749 1.35m0 0a6.772 6.772 0 01-3.044 0"
                />
              </svg>
            </a>
          </li>
          <li>
            <a
              href="/create-goals"
              aria-label="create goals"
              title="Create Goals"
              class={$page.url.pathname === '/create-goals' ? 'rounded bg-white' : ''}
              on:click={animateSVG}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="stroke-current {$page.url.pathname === '/create-goals'
                  ? 'text-primary'
                  : 'text-white'} h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M12 9v6m3-3H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
            </a>
          </li>
          <li>
            <a
              href="/account-settings"
              aria-label="account-settings"
              title="Account Settings"
              class={$page.url.pathname === '/account-settings' ? 'rounded bg-white' : ''}
              on:click={animateSVG}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="stroke-current {$page.url.pathname === '/account-settings'
                  ? 'text-primary'
                  : 'text-white'} h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M10.5 6h9.75M10.5 6a1.5 1.5 0 11-3 0m3 0a1.5 1.5 0 10-3 0M3.75 6H7.5m3 12h9.75m-9.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-3.75 0H7.5m9-6h3.75m-3.75 0a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m-9.75 0h9.75"
                />
              </svg>
            </a>
          </li>
        {/if}
      </ul>
    </div>

    <div class="flex-1 px-2 mx-2" />
    <div class="flex-none">
      <ul class="menu menu-horizontal px-1" />
      <ThemeSelector />
    </div>
  </div>
</div>

<style>
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  .page-fade-in {
    animation: fadeIn 1s ease-in-out;
  }
</style>
