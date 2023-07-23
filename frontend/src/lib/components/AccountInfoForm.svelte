<script lang="ts">
  import { navigate } from 'svelte-routing';
  import { onMount } from 'svelte';
  import { createUser, getMe, login } from '$lib/api';
  import type { UserCreate } from '$lib/generated';
  import type { UserLogin } from '$lib/types';
  import { LoginError } from '$lib/errors';
  import { isLoading, isLoggedIn, accessToken } from '$lib/stores/stores';
  import Input from '$lib/components/Input.svelte';
  import ErrorMessage from '$lib/components/ErrorMessage.svelte';

  let user = {
    userName: null,
    avatar: null,
    firstName: null,
    lastName: null,
    country: null,
    password: null,
    verifyPassword: null
  };

  let genericError = false;
  let genericErrorMessage = '';
  let passwordVerifyError = false;
  let firstNameError = false;
  let lastNameError = false;
  let userNameError = false;
  let passwordError = false;
  let countryError = false;

  function isMissing(check: string | null): boolean {
    if (check == null || check.trim() === '') {
      return true;
    }

    return false;
  }

  async function logOut() {
    accessToken.set(null);
    navigate('/');
    window.location.reload();
  }

  async function handleSubmit() {
    isLoading.set(true);
    firstNameError = isMissing(user.firstName);
    lastNameError = isMissing(user.lastName);
    userNameError = isMissing(user.userName);
    passwordError = isMissing(user.password);
    countryError = isMissing(user.country);

    if (!passwordError && user.password !== user.verifyPassword) {
      isLoading.set(false);
      passwordVerifyError = true;
    } else {
      passwordVerifyError = false;
    }

    if (
      firstNameError === true ||
      lastNameError === true ||
      userNameError === true ||
      passwordError === true ||
      countryError === true ||
      passwordVerifyError === true
    ) {
      isLoading.set(false);
      return;
    }

    // This is already checked, but typescript refuses to believe it without this.
    if (user.firstName && user.lastName && user.userName && user.country && user.password) {
      const userCreate: UserCreate = {
        first_name: user.firstName,
        last_name: user.lastName,
        user_name: user.userName,
        country: user.country,
        password: user.password
      };

      if (user.avatar) {
        userCreate['avatar_url'] = user.avatar;
      }

      try {
        await createUser(userCreate);
      } catch (error) {
        genericError = true;
        genericErrorMessage =
          'An error occurred trying to connect to the sever. Please try again later.';
      }

      let userLogin: UserLogin = {
        userName: user.userName,
        password: user.password
      };

      try {
        const token = await login(userLogin);
        accessToken.set(token);
      } catch (error) {
        if (
          error instanceof LoginError &&
          error.message !== undefined &&
          error.message === 'Incorrect user name or password'
        ) {
          genericError = true;
          genericErrorMessage = 'Incorrect user name or password';
        } else {
          genericError = true;
          genericErrorMessage =
            'An error occurred trying to connect to the sever. Please try again later.';
        }
      }
    } else {
      genericError = true;
      genericErrorMessage = 'An error occurred trying to create the user. Please try again later.';
    }

    isLoading.set(false);
  }

  onMount(async () => {
    let token: AccessToken | null;
    accessToken.subscribe((value: AccessToken | null) => (token = value));

    if (token != null) {
      const info = await getMe();
      user.firstName = info.first_name;
      user.lastName = info.last_name;
      user.userName = info.user_name;
      user.country = info.country;

      if (info.avatar_url !== undefined) {
        user.avatar = info.avatar_url;
      }
    }
  });
</script>

<form
  on:submit|preventDefault={handleSubmit}
  class="w-full max-w-lg mx-auto my-10 p-5 rounded shadow"
>
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full md:w-1/2 px-3 mb-6 md:mb-0">
      <Input
        inputId="first-name"
        labelText="First Name*"
        placeholder="first name"
        errorMessage="First Name is required."
        isError={firstNameError}
        bind:value={user.firstName}
      />
    </div>
    <div class="w-full md:w-1/2 px-3">
      <Input
        inputId="last-name"
        labelText="Last Name*"
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
        labelText="User Name*"
        placeholder="user name"
        errorMessage="User Name is required."
        isError={userNameError}
        bind:value={user.userName}
      />
    </div>
    <div class="w-full md:w-1/2 px-3">
      <Input
        inputId="country"
        labelText="Country"
        placeholder="country"
        bind:value={user.country}
      />
    </div>
  </div>
  <div class="flex flex-wrap -mx-3 mb-6">
    <div class="w-full md:w-1/2 px-3">
      <Input
        inputId="password"
        labelText="Password*"
        placeholder="password"
        errorMessage="Password is required."
        isError={passwordError}
        isPassword={true}
        bind:value={user.password}
      />
    </div>
    <div class="w-full md:w-1/2 px-3">
      <Input
        inputId="verify-password"
        labelText="Verify Password*"
        placeholder="verify password"
        isPassword={true}
        bind:value={user.verifyPassword}
      />
    </div>
    {#if passwordVerifyError}
      <div class="w-full text-center">
        <ErrorMessage
          errorMessageId="password-verify-error"
          errorMessage="Passwords don't match"
          showError={passwordVerifyError}
        />
      </div>
    {/if}
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
  <ErrorMessage
    errorMessageId="generic-error"
    errorMessage={genericErrorMessage}
    showError={genericError}
  />
  <div class="flex items-center justify-between">
    {#if $isLoggedIn}
      <div class="ml-2">
        <button class="btn btn-primary" type="submit" id="btnSubmit">Save</button>
      </div>
      <div>
        <button class="btn btn-secondary" on:click={() => logOut()}>Log Out</button>
      </div>
    {:else if $isLoading}
      <div class="mt-6 text-center">
        <span class="loading loading-spinner text-primary" />
      </div>
    {:else}
      <button class="btn btn-primary" type="submit" id="btnSubmit">Sign Up</button>
    {/if}
  </div>
</form>
