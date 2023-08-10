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
              class={$page.url.pathname === '/' ? 'rounded bg-white' : ''}
              on:click={animateSVG}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="stroke-current {$page.url.pathname === '/'
                  ? 'text-primary'
                  : 'text-white'} h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
                />
              </svg>
            </a>
          </li>
        {:else}
          <li>
            <a
              href="/"
              aria-label="home"
              title="Home"
              class={$page.url.pathname === '/' ? 'rounded bg-white' : ''}
              on:click={animateSVG}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                class="stroke-current {$page.url.pathname === '/'
                  ? 'text-primary'
                  : 'text-white'} h-5 w-5"
                fill="none"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M2.25 12l8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
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
              aria-label="account settings"
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
