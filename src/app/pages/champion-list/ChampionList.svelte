<script lang="ts">
  import Champion from "../../components/champion/Champion.svelte";
  import { beforeUpdate } from "svelte";
  import champList from '../../../assets/data/lolchampions.json';

  export let listType: string;
</script>

<div class="content">
  {#each champList as champ}
    <Champion {champ} />
  {/each}
</div>

<style>
  .content {
    width: 100%;
    background-color: white;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
  }
</style>
