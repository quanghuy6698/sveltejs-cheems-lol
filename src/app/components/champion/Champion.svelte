<script lang="ts">
  import { beforeUpdate } from "svelte";

  export let champ;
  let champImg;

  beforeUpdate(() => {
    champImg = './img/cheems-lol/' + champ.img;
  });


  function errImg(){
    champImg = './img/cheems-lol/cheems.png';
  }
</script>

<div class="champion">
  <div
    class="champion__content-wrapper"
    style="background-image: url({champImg});"
    on:error={errImg} 
  >
    <div class="champion__name">{champ.name}</div>
  </div>
</div>


<style>
  .champion {
    background-color: transparent;
    width: 300px;
    height: 300px;
    padding: 4px;
  }

  .champion__content-wrapper {
    background-size: cover;
    width: 276px;
    height: 276px;
    border-bottom-left-radius: 22px;
    border-top-right-radius: 22px;
    padding: 8px;
    box-shadow: 2px 2px #808080;
    position: relative;
  }

  .champion__name {
    background-color: black;
    color: white;
    font-size: 24px;
    font-weight: 600;
    padding: 8px;
    position: absolute;
    bottom: 0px;
    right: 0px;
    width: 80%;
    border-top-left-radius: 8px;
  }
</style>
