<script context="module">
	export const prerender = false;
</script>

<script>
	import Welcome from '$lib/Welcome.svelte';
	import { session } from '$app/stores';
	// import BoardList from '$lib/BoardList.svelte';
</script>

<svelte:head>
	<title>Home</title>
</svelte:head>

{#if $session.user}
	<!-- <BoardList /> -->
{:else}
	<Welcome />
{/if}

<style>
	.content {
		max-width: 880px;
		margin: 20px auto;
		padding: 40px;
	}

	h1 {
		width: 100%;
		text-align: center;
	}
	pre code {
		background-color: #eee;
		border: 1px solid #999;
		display: block;
		padding: 20px;
		max-width: 100%;
		margin: 10px auto;
	}
</style>
