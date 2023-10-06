<template>
  <button @click="convertToGreyscale" class="inline-block bg-blue-500 text-white px-4 py-2 cursor-pointer rounded">
    Convert to Greyscale
  </button>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  props: {
    imageUrl: String
  },
  methods: {
    async convertToGreyscale() {
      try {
        // Fetch the image from its URL
        const imageResponse = await fetch(this.imageUrl);
        const imageBlob = await imageResponse.blob();

        // Create a FormData object and append the image
        const formData = new FormData();
        formData.append('original_image', imageBlob, 'uploaded_image.jpg');

        // Send the image data to the backend
        const response = await fetch('http://localhost:8000/api/upload/', {
          method: 'POST',
          body: formData
        });

        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        console.log(data);
        this.$emit('updateImageUrl', data.greyscale_image);  // Update the parent component's imageUrl to the greyscale image URL

      } catch (error) {
        console.error('Error converting image to greyscale:', error);
      }
    }
  }
});
</script>
