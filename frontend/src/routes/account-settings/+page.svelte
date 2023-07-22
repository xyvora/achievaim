<script>
    import Signup from '$lib/components/signup.svelte';
    import { isLoggedIn, accessToken } from '$lib/stores/stores';

    async function logOut() {
        accessToken.set(null);
    }
</script>

<main>
    <Signup />
    {#if $isLoggedIn}
    <div class="ml-2">
        <button class="px-4 py-2 text-red-500 bg-transparent border border-red-500 hover:bg-red-500 hover:text-white rounded-lg focus:outline-none transition-colors duration-200 ease-in-out" on:click={() => logOut()}>Log Out</button>
    </div>
    {/if}
</main>
