<script lang="ts">
  import { createUser } from '$lib/api';
  import type { User } from '$lib/types';
  import { isLoggedIn, accessToken } from '$lib/stores/stores';
  import Input from '$lib/components/Input.svelte';

  let user: User = {
    username: null,
    avatar: null,
    firstName: null,
    lastName: null,
    country: null,
    password: null
  };

  let genericError = false;
  let firstNameError = false;
  let lastNameError = false;
  let userNameError = false;
  let passwordError = false;

  async function logOut() {
    accessToken.set(null);
  }
</script>

<form class="w-full max-w-lg mx-auto my-10 p-5 rounded shadow">
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
      <Input
        inputId="first-name"
        labelText="First Name"
        placeholder="first name"
        errorMessage="First Name is required."
        isError={firstNameError}
        bind:value={user.firstName}
      />
    </div>
    <div class="w-full md:w-1/2 px-3">
      <Input
        inputId="last-name"
        labelText="Last Name"
        placeholder="last name"
        errorMessage="Last Name is required."
        isError={lastNameError}
        bind:value={user.lastName}
      />
    </div>
  </div>
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
      <Input
        inputId="user-name"
        labelText="User Name"
        placeholder="user name"
        errorMessage="User Name is required."
        isError={userNameError}
        bind:value={user.userName}
      />
    </div>
    <div class="w-full md:w-1/2 px-3">
      <Input
        inputId="password"
        labelText="Password"
        placeholder="password"
        errorMessage="Password is required."
        isError={passwordError}
        isPassword={true}
        bind:value={user.password}
      />
    </div>
  </div>
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full px-3">
      <Input
        inputId="country"
        labelText="Country"
        placeholder="country"
        bind:value={user.country}
      />
    </div>
  </div>
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full px-3">
      <Input
        inputId="avatar"
        labelText="Avatar Photo URL"
        placeholder="avatar photo url"
        bind:value={user.avatar}
      />
    </div>
  </div>
  <div class="flex items-center justify-between">
    <button class="btn btn-primary" type="submit" id="btnSubmit">Sign Up</button>
    {#if $isLoggedIn}
      <div class="ml-2">
        <button
          class="px-4 py-2 text-white bg-red-500 rounded-lg focus:outline-none hover:bg-red-600 active:bg-red-700 transition-colors duration-200 ease-in-out"
          on:click={() => logOut()}>Log Out</button
        >
      </div>
    {/if}
  </div>
</form>
