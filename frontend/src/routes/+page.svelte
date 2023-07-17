<script lang="ts">
  import { page } from '$app/stores';
  import Input from '$lib/components/Input.svelte';
  import type { UserLogin } from '$lib/types';
  import { login } from '$lib/api';

  let userLogin: UserLogin = {
    userName: '',
    password: ''
  };

  let userNameError = false;
  let passwordError = false;

  async function handleSubmit() {
    if (userLogin.userName == null || userLogin.userName.trim() === '') {
      userNameError = true;
    } else {
      userNameError = false;
    }

    if (userLogin.password == null || userLogin.password.trim() === '') {
      passwordError = true;
    } else {
      passwordError = false;
    }

    if (userNameError === true || passwordError === true) {
      return;
    }

    const token = await login(userLogin);
    console.log(token);
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
    <div class="card flex-shrink-0 w-full lg:w-1/3 max-w-sm shadow-2xl bg-base-100">
      <div class="card-body">
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

        <div class="form-control">
          <a href={'#'} class="label-text-alt link link-hover mt-4 mb-4">Forgot password?</a>
          <a
            href="signup"
            class="label-text-alt link link-hover"
            class:active={$page.url.pathname === '/signup'}
            >Are your Goals Smart yet? Sign up here!</a
          >
        </div>
        <div class="form-control mt-6">
          <button class="btn btn-primary" on:click={() => handleSubmit()} id="login-button"
            >Login</button
          >
        </div>
        <div class="form-control mt-6 text-center text-lg font-bold" />
      </div>
    </div>
  </div>
</div>
