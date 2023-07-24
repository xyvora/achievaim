<script lang="ts">
  import { page } from '$app/stores';
  import ErrorMessage from '$lib/components/ErrorMessage.svelte';
  import Input from '$lib/components/Input.svelte';
  import { LoginError } from '$lib/errors';
  import { accessToken, isLoading, isLoggedIn } from '$lib/stores/stores';
  import type { UserLogin } from '$lib/types';
  import { login } from '$lib/api';

  let userLogin: UserLogin = {
    userName: '',
    password: ''
  };

  let userNameError = false;
  let passwordError = false;
  let genericError = false;
  let genericErrorMessage = '';

  async function handleSubmit() {
    isLoading.set(true);
    genericError = false;
    userNameError = false;
    passwordError = false;

    if (userLogin.userName == null || userLogin.userName.trim() === '') {
      userNameError = true;
    }

    if (userLogin.password == null || userLogin.password.trim() === '') {
      passwordError = true;
    }

    if (userNameError === true || passwordError === true) {
      isLoading.set(false);
      return;
    }

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
      isLoading.set(false);
      return;
    }
    userLogin.userName = '';
    userLogin.password = '';
    isLoading.set(false);
  }
</script>

<div class="hero min-h-screen bg-base-200 mb-10">
  <div class="flex flex-col lg:flex-row justify-around items-center lg:items-start hero-content">
    <div class="text-center lg:text-left lg:w-1/2">
      <h1 class="text-5xl font-bold">Smart Tracking Your Goals.</h1>
      <p class="py-6">
        SMART Goal AI is a sophisticated tool leveraging artificial intelligence to assist users in
        formulating, tracking, and accomplishing their goals using the SMART (Specific, Measurable,
        Achievable, Relevant, Time-bound) methodology. It refines users' goals for clarity and
        realism and integrates features for tracking progress, including customizable reminders. The
        app promotes consistent habits by enabling users to schedule daily reminders, creating an
        effective and efficient platform for personal and professional growth.
      </p>
    </div>
    {#if !$isLoggedIn}
      <div class="card flex-shrink-0 w-full lg:w-1/3 max-w-sm shadow-2xl bg-base-100">
        <div class="card-body">
          <form
            on:submit|preventDefault={handleSubmit}
            class="w-full max-w-lg mx-auto my-10 p-5 rounded shadow"
          >
            <Input
              inputId="user-name"
              labelText="User Name"
              placeholder="user name"
              errorMessage="User Name is required."
              isError={userNameError}
              bind:value={userLogin.userName}
            />

            <Input
              inputId="password"
              labelText="Password"
              placeholder="password"
              errorMessage="Password is required."
              isError={passwordError}
              bind:value={userLogin.password}
              isPassword={true}
            />

            <ErrorMessage
              errorMessageId="generic-error"
              errorMessage={genericErrorMessage}
              showError={genericError}
            />

            <div class="form-control">
              <a href={'#'} class="label-text-alt link link-hover mt-4 mb-4">Forgot password?</a>
              <a
                href="signup"
                class="label-text-alt link link-hover"
                class:active={$page.url.pathname === '/signup'}
                >Are your Goals Smart yet? Sign up here!</a
              >
            </div>
            {#if $isLoading}
              <div class="mt-6 text-center">
                <span class="loading loading-spinner text-primary" id="login-spinner" />
              </div>
            {:else}
              <div class="form-control mt-6">
                <button class="btn btn-primary" type="submit" id="login-button">Login</button>
              </div>
            {/if}
            <div class="form-control mt-6 text-center text-lg font-bold" />
          </form>
        </div>
      </div>
    {/if}
  </div>
</div>
