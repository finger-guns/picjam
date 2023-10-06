<template>
  <div class="h-screen flex flex-col justify-center items-center space-y-4">
    <!-- Images container -->
    <div class="flex w-4/5 justify-center items-center space-x-4">
      <!-- Original Image -->
      <div v-if="originalImageUrl" class="flex-shrink-0 w-1/2">
        <img :src="originalImageUrl" alt="Original Image" class="w-full h-auto">
      </div>

      <!-- Greyscale Image -->
      <div v-if="greyscaleImageUrl" class="flex-shrink-0 w-1/2">
        <img :src="backendUrl + greyscaleImageUrl" alt="Greyscale Image" class="w-full h-auto">
      </div>
    </div>

    <!-- Buttons container -->
    <div class="flex space-x-4 mt-4 justify-center w-full">
      <ImageUploader @update="updateOriginalImageUrl"/>
      <div v-if="originalImageUrl">
        <GreyscaleButton :imageUrl="originalImageUrl" @updateImageUrl="updateGreyscaleImageUrl"/>
      </div>
    </div>
  </div>
</template>



<script lang="ts">
import { ref } from 'vue';
import ImageUploader from './components/ImageUploader.vue';
import GreyscaleButton from './components/GreyScale.vue';

export default {
  components: {
    ImageUploader,
    GreyscaleButton
  },
  setup() {
    const backendUrl = 'http://localhost:8000';
    const originalImageUrl = ref<string | null>(null);
    const greyscaleImageUrl = ref<string | null>(null);

    const updateOriginalImageUrl = (url: string) => {
      originalImageUrl.value = url;
    };

    const updateGreyscaleImageUrl = (url: string) => {
      greyscaleImageUrl.value = url;
    };

    return {
      backendUrl,
      originalImageUrl,
      greyscaleImageUrl,
      updateOriginalImageUrl,
      updateGreyscaleImageUrl
    };
  }
};
</script>
