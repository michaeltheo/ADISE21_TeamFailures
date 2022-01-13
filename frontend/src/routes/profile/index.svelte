<script context="module">
	export async function load({ fetch, session }) {
		if (!session.user) {
			return {
				status: 302,
				redirect: '/login'
			};
		}

		if (!session.user.name) {
			const res = await fetch('/user');
			const user = await res.json();
			session.user = {
				uid: user.id,
				name: user.name,
				email: user.email
			};
		}

		return {
			props: {
				name: session.user.name,
				email: session.user.email,
				token: session.token
			}
		};
	}
</script>

<script>
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { session } from '$app/stores';
	import { List, ListGroup, ListItem, Icon } from 'svelte-materialify';
	import { mdiAccount, mdiEmail, mdiShieldLock, mdiChevronUp, mdiExitRun } from '@mdi/js';

	export let email;
	export let name;
	export let token;
	let active = false;
	/*
	let name

	onMount(async () => {
		const res = await fetch('/user')
		const user = await res.json()
		name = user.name
	})
    */

	async function logout() {
		const res = await fetch('/auth/logout', {
			method: 'POST'
		});
		$session.user = null;
		goto('/');
	}
</script>

<svelte:head>
	<title>Profile</title>
</svelte:head>

<div class="content d-flex justify-center">
	<List class="elevation-3" style="width:600px">
		<ListItem>
			<span slot="prepend">
				<Icon path={mdiAccount} size="40px" />
			</span>
			<div style="font-size: 150% ;">
				{name}
			</div>
		</ListItem>
		<ListItem>
			<span slot="prepend">
				<Icon path={mdiEmail} size="40px" />
			</span>
			<div style="font-size: 150% ;">
				{email}
			</div>
		</ListItem>

		<ListItem>
			<span slot="prepend">
				<Icon path={mdiExitRun} size="40px" />
			</span>
			<button on:click={logout} style="width: 496px;">
				<p style="text-align: left; font-size:150%">Log Out</p>
			</button>
		</ListItem>
		<ListGroup bind:active offset={72}>
			<span slot="prepend">
				<Icon path={mdiShieldLock} size="40px" />
			</span>
			<span slot="activator"> <div style="font-size: 150% ;">Token</div></span>
			<span slot="append">
				<Icon path={mdiChevronUp} rotate={active ? 0 : 180} size="40px" />
			</span>
			<ListItem>
				<div style="font-size: 80%;">
					{token}
				</div>
			</ListItem>
		</ListGroup>
	</List>
	<!-- <h1>Profile</h1>
	<p>Hello {name} you are logged in with the email {email}, token {token}</p>
	<button on:click={logout}>log out</button> -->
</div>

<style>
	.content {
		padding: 40px;
	}

	h1 {
		margin-top: 0;
	}

	button {
		border-radius: 12px;
		width: 100px;
		/* color: #fff; */
	}
	button:hover {
		color: #000;
		background-color: rgb(154, 211, 242);
	}
</style>
