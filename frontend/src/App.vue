<template>
    <div class="flex flex-nowrap space-x-8">
      <div v-if="greyscaleImageUrl" class="flex-auto space-x-8">
        <img :src="backendUrl + greyscaleImageUrl"/>
      </div>

      <div v-if="originalImageUrl" class="flex-initial">
        <img :src="backendUrl + originalImageUrl"/>
      </div>  
    </div>
    <div class="space-y-10 flex">
      <div>
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
