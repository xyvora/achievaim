<script lang="ts">
  import type { PasswordReset } from '$lib/generated';
  import Message from '$lib/components/Message.svelte';
  import Input from '$lib/components/Input.svelte';
  import { isLoading } from '$lib/stores/stores';
  import { forgotPassword } from '$lib/api';

  interface ResetInfo {
    userName: string;
    securityAnswer: string;
    newPassword: string;
    verifyNewPassword: string;
  }

  let resetInfo: ResetInfo = {
    userName: '',
    securityAnswer: '',
    newPassword: '',
    verifyNewPassword: '',
  };

  let userNameError = false;
  let securityAnswerError = false;
  let newPasswordError = false;
  let verifyPasswordError = false;
  let genericError = false;
  let genericErrorMessage = '';
  let showSuccess = false;

  async function handleSubmit() {
    isLoading.set(true);
    genericError = false;
    userNameError = false;
    securityAnswerError = false;
    newPasswordError = false;
    verifyPasswordError = false;

    if (resetInfo.userName.trim() === '') {
      userNameError = true;
    }

    if (resetInfo.securityAnswer.trim() === '') {
      securityAnswerError = true;
    }

    if (resetInfo.newPassword.trim() === '') {
      newPasswordError = true;
    }

    if (!newPasswordError && resetInfo.newPassword !== resetInfo.verifyNewPassword) {
      isLoading.set(false);
      verifyPasswordError = true;
    } else {
      verifyPasswordError = false;
    }

    if (
      userNameError === true ||
      securityAnswerError ||
      newPasswordError === true ||
      verifyPasswordError === true
    ) {
      isLoading.set(false);
      return;
    }

    try {
      const payload: PasswordReset = {
        user_name: resetInfo.userName,
        security_question_answer: resetInfo.securityAnswer,
        new_password: resetInfo.newPassword,
      };
      await forgotPassword(payload);
      showSuccess = true;
      console.log(showSuccess);
      isLoading.set(false);
    } catch (error) {
      genericError = true;
      genericErrorMessage =
        'An error occurred trying to connect to the sever. Please try again later.';
      showSuccess = true;
      isLoading.set(false);
      return;
    }

    resetInfo.userName = '';
    resetInfo.securityAnswer = '';
    resetInfo.newPassword = '';
    resetInfo.verifyNewPassword = '';
    isLoading.set(false);
  }
</script>

<div class="page-fade-in flex items-center justify-center min-h-screen">
  <form
    on:submit|preventDefault={handleSubmit}
    class="container shadow-lg rounded-xl mb-8 mx-4 px-4 pt-5 sm:mx-auto sm:px-6 md:px-8 md:max-w-xl lg:max-w-3xl z-10"
  >
    <figure>
      <figcaption class="p-4 card-body flex flex-col space-y-8">
        <h1 class="mb-3 text-xl leading-tight tracking-tight">Forgot your password?</h1>
        <p>Enter your user name and the answer to your security question below</p>
        <div class="flex flex-wrap -mx-3 mb-8">
          <div class="w-full px-3 mb-4 sm:mb-6">
            <Input
              inputId="user-name"
              labelText="User Name*"
              placeholder="user name"
              errorMessage="User Name is required."
              isError={userNameError}
              bind:value={resetInfo.userName}
            />
          </div>
          <div class="w-full px-3 mb-4 sm:mb-6">
            <Input
              inputId="security-answer"
              labelText="If you could have any superpower, what would it be?*"
              placeholder="flying"
              errorMessage="Security answer is required."
              isError={securityAnswerError}
              bind:value={resetInfo.securityAnswer}
            />
          </div>
          <div class="w-full px-3 mb-4 sm:mb-6">
            <Input
              inputId="new-password"
              labelText="New Password*"
              placeholder="password"
              isPassword={true}
              errorMessage="New password is required."
              isError={newPasswordError}
              bind:value={resetInfo.newPassword}
            />
          </div>
          <div class="w-full px-3 mb-4 sm:mb-6">
            <Input
              inputId="verify-new-password"
              labelText="Verify New Password*"
              placeholder="password"
              isPassword={true}
              errorMessage="Passwords do not match."
              isError={verifyPasswordError}
              bind:value={resetInfo.verifyNewPassword}
            />
          </div>
        </div>
        <div class="flex item-center mb-8">
          <button type="submit" class="btn btn-primary" id="btn-reset">Reset password</button>
        </div>
        <Message
          messageId="successful-reset"
          message="Password successfully reset"
          showMessage={showSuccess}
        />
        <Message
          messageId="generic-error"
          message={genericErrorMessage}
          showMessage={genericError}
          isError={true}
        />
      </figcaption>
    </figure>
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
