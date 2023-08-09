<script lang="ts">
  import { goto } from '$app/navigation';
  import { onMount } from 'svelte';
  import { createUser, deleteMe, getMe, login, updateMe } from '$lib/api';
  import type { UserCreate, UserUpdateMe } from '$lib/generated';
  import type { AccessToken, UserLogin } from '$lib/types';
  import { LoginError } from '$lib/errors';
  import { isLoading, isLoggedIn, accessToken } from '$lib/stores/stores';
  import Input from '$lib/components/Input.svelte';
  import ErrorMessage from '$lib/components/ErrorMessage.svelte';

  interface User {
    id?: string;
    userName: string | null;
    firstName: string | null;
    lastName: string | null;
    country: string | null;
    password: string | null;
    verifyPassword: string | null;
    securityQuestionAnswer: string | null;
  }

  let user: User = {
    userName: null,
    firstName: null,
    lastName: null,
    country: null,
    password: null,
    verifyPassword: null,
    securityQuestionAnswer: null,
  };

  let genericError = false;
  let genericErrorMessage = '';
  let passwordVerifyError = false;
  let firstNameError = false;
  let lastNameError = false;
  let userNameError = false;
  let passwordError = false;
  let securityQuestionAnswerError = false;

  function isMissing(check: string | null): boolean {
    if (check == null || check.trim() === '') {
      return true;
    }

    return false;
  }

  async function deleteUser() {
    if (
      window.confirm('Are you sure you want to delete your information? This cannot be undone.')
    ) {
      try {
        await deleteMe();
        await logOut();
      } catch (error) {
        console.log(error);
        genericError = true;
        genericErrorMessage =
          'An error occurred trying to delete the information. Please try again later.';
      }
    }
  }

  async function logOut() {
    accessToken.set(null);
    goto('/');
  }

  async function handleSubmit() {
    isLoading.set(true);
    firstNameError = isMissing(user.firstName);
    lastNameError = isMissing(user.lastName);
    userNameError = isMissing(user.userName);
    passwordError = isMissing(user.password);
    securityQuestionAnswerError = isMissing(user.securityQuestionAnswer);

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
      passwordVerifyError === true ||
      securityQuestionAnswerError === true
    ) {
      isLoading.set(false);
      return;
    }

    const token: AccessToken | null = await new Promise<AccessToken | null>((resolve) => {
      accessToken.subscribe((value: AccessToken | null) => resolve(value));
    });

    if (token) {
      // This is already checked, but typescript refuses to believe it without this.
      if (
        user.id &&
        user.firstName &&
        user.lastName &&
        user.userName &&
        user.country &&
        user.password &&
        user.securityQuestionAnswer
      ) {
        const userUpdate: UserUpdateMe = {
          id: user.id,
          first_name: user.firstName,
          last_name: user.lastName,
          user_name: user.userName,
          country: user.country,
          password: user.password,
          security_question_answer: user.securityQuestionAnswer,
        };

        try {
          await updateMe(userUpdate);
        } catch (error) {
          console.log(error);
          genericError = true;
          genericErrorMessage =
            'An error occurred trying to connect to the sever. Please try again later.';
          isLoading.set(false);
          return;
        }
      } else {
        genericError = true;
        genericErrorMessage =
          'An error occurred trying to create the user. Please try again later.';
        isLoading.set(false);
        return;
      }
    } else {
      // This is already checked, but typescript refuses to believe it without this.
      if (
        user.firstName &&
        user.lastName &&
        user.userName &&
        user.password &&
        user.securityQuestionAnswer
      ) {
        const userCreate: UserCreate = {
          first_name: user.firstName,
          last_name: user.lastName,
          user_name: user.userName,
          password: user.password,
          security_question_answer: user.securityQuestionAnswer,
        };

        if (user.country) {
          userCreate['country'] = user.country;
        }

        try {
          await createUser(userCreate);
        } catch (error) {
          console.log(error);
          genericError = true;
          genericErrorMessage =
            'An error occurred trying to connect to the sever. Please try again later.';
          isLoading.set(false);
          return;
        }

        let userLogin: UserLogin = {
          userName: user.userName,
          password: user.password,
        };

        try {
          const token = await login(userLogin);
          accessToken.set(token);
        } catch (error) {
          console.log(error);
          if (
            error instanceof LoginError &&
            error.message !== undefined &&
            error.message === 'Incorrect user name or password'
          ) {
            genericError = true;
            genericErrorMessage = 'Incorrect user name or password';
            isLoading.set(false);
            return;
          } else {
            genericError = true;
            genericErrorMessage = `An error occurred trying to connect to the sever. Please try again later.`;
            isLoading.set(false);
            return;
          }
        }
        goto('/account-settings');
      } else {
        genericError = true;
        genericErrorMessage =
          'An error occurred trying to create the user. Please try again later.';
        isLoading.set(false);
        return;
      }
    }

    isLoading.set(false);
  }

  onMount(async () => {
    const token: AccessToken | null = await new Promise<AccessToken | null>((resolve) => {
      accessToken.subscribe((value: AccessToken | null) => resolve(value));
    });

    if (token) {
      const info = await getMe();
      user.id = info.id;
      user.firstName = info.first_name;
      user.lastName = info.last_name;
      user.userName = info.user_name;

      if (info.country) {
        user.country = info.country;
      }
    }
  });
</script>

<div class="page-fade-in">
  <form
    on:submit|preventDefault={handleSubmit}
    class="w-full max-w-lg mx-auto my-10 p-5 rounded shadow"
  >

    <div class="md:flex mb-6">
      <div class="w-full md:w-1/2 md:mr-4 mb-6 md:mb-0">
        <Input
          inputId="first-name"
          labelText="First Name*"
          placeholder="first name"
          errorMessage="First Name is required."
          isError={firstNameError}
          bind:value={user.firstName}
        />
      </div>
      <div class="w-full md:w-1/2 md:ml-4 mb-6">
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

    <div class="md:flex mb-6">
      <div class="w-full md:w-1/2 md:mr-4 mb-6 md:mb-0">
        <Input
          inputId="user-name"
          labelText="User Name*"
          placeholder="user name"
          errorMessage="User Name is required."
          isError={userNameError}
          bind:value={user.userName}
        />
      </div>
      <div class="w-full md:w-1/2 md:ml-4 mb-6">
        <Input
          inputId="country"
          labelText="Country"
          placeholder="country"
          bind:value={user.country}
        />
      </div>
    </div>

    <div class="mb-6">
      <Input
        inputId="security-question-answer"
        labelText="If you could have any superpower, what would it be?*"
        placeholder="superpower"
        errorMessage="Security question is required."
        isError={securityQuestionAnswerError}
        bind:value={user.securityQuestionAnswer}
      />
    </div>

    <div class="md:flex mb-6">
      <div class="w-full md:w-1/2 md:mr-4 mb-6 md:mb-0">
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
      <div class="w-full md:w-1/2 md:ml-4 mb-6">
        <Input
          inputId="verify-password"
          labelText="Verify Password*"
          placeholder="verify password"
          isPassword={true}
          bind:value={user.verifyPassword}
        />
      </div>
    </div>

    {#if passwordVerifyError}
    <div class="mb-6">
      <ErrorMessage
        errorMessageId="password-verify-error"
        errorMessage="Passwords don't match"
        showError={passwordVerifyError}
      />
    </div>
    {/if}

    <div class="mb-6">
      <ErrorMessage
        errorMessageId="generic-error"
        errorMessage={genericErrorMessage}
        showError={genericError}
      />
    </div>
    
    <div class="flex flex-col md:flex-row md:justify-between mb-6 space-y-2 md:space-y-0 md:space-x-2">
      {#if $isLoggedIn}
          <button class="btn btn-primary mb-2 md:mb-0" type="submit" id="btn-save">Save</button>
          <button class="btn btn-outline mb-2 md:mb-0 mx-auto md:mx-0" type="button" id="btn-log-out" on:click={() => logOut()}>Log Out</button>
          <button class="btn btn-outline mb-2 md:mb-0 ml-auto md:ml-0" type="button" id="btn-delete" on:click={() => deleteUser()}>Delete</button>
      {:else if $isLoading}
          <span class="loading loading-spinner text-primary mt-6 md:mt-0" id="sign-up-spinner" />
      {:else}
          <button class="btn btn-primary mb-2 md:mb-0" type="submit" id="btn-sign-up">Sign Up</button>
      {/if}
  </div>
  
  </form>
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
