<script lang="ts">
  let name = "Svelte.js";
</script>

<div class="container">
  <div class="title">
    <h1 class="title__text">Hello {name}</h1>
  </div>

  <div class="content">
    <div class="content-item">
      <div class="content-item__img" />
      <div class="content-item__content">
        dsk dsf dsdslj sdfhdskf dhfudsu dsufdsfhsd
      </div>
    </div>
  </div>
</div>

<style>
  @media screen and (max-width: 600px) {
    .container {
      width: 96%;
      margin: 0 auto;
      background-color: #ccc;
    }
  }

  @media screen and (min-width: 600px) {
    .container {
      width: 600px;
      margin: 0 auto;
      background-color: #ccc;
    }
  }

  .title {
    background-color: #ffffff;
    border-radius: 8px;
    margin-top: 8px;
    padding: 16px;
  }

  .title__text {
    color: tomato;
  }

  .content {
    background-color: #ffffff;
    margin-top: 8px;
    border-radius: 8px;
    padding: 16px;

    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }

  .content-item {
    background-color: aqua;
    width: 300px;
    height: 300px;
    padding: 8px;
    border-radius: 8px;
  }

  .content-item__img {
    float: left;
    width: 150px;
  }

  .content-item__content {
    background-color: aqua;
    padding: 8px;
  }
</style>
