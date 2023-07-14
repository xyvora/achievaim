import { expect, test } from '@playwright/test';

test('page loads', async ({ page }) => {
  await page.goto('/account');
  await expect(page.locator('#navbar')).toBeVisible();
});

test('first name required', async ({ page }) => {
  await page.goto('/account');
  await page.locator('input#first-name[required]');
});

test('last name required', async ({ page }) => {
  await page.goto('/account');
  await page.locator('input#last-name[required]');
});

test('username required', async ({ page }) => {
  await page.goto('/account');
  await page.locator('input#username[required]');
});
