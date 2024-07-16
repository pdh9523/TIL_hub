<template>
  <div>
    <p class="greeting"> {{msg}} </p>
  </div>
</template>

<script setup>
import {ref} from 'vue'
/**
* a에서 b를 나눔
* @param {number} a 제수
* @param {number} b 피제수
*
* @return {number} a에서 b를 나눈 값을 반환
*/
function divide(a, b) {
	return (a/b)
}
const msg = ref('Hello World!')
</script>

<style scoped>
  .greeting {
    color : crimson;
  }
</style>