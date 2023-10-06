<template>
  <div>
    <div>
      <div v-if="!imageUrl" class="mb-4">No image selected</div>
      <img v-if="imageUrl" :src="imageUrl" alt="Uploaded Image" class="" />
      <label class="file-input-label inline-block bg-green-500 text-white px-4 py-2 cursor-pointer rounded mb-4">
        Input File
        <input type="file" @change="onFileChange" class="hidden" />
      </label>
    </div>
  </div>
</template>

<script lang="ts">
import { ref, defineComponent } from 'vue';
//probably needs some props.
export default defineComponent({
  emits: ['update'],
  setup(_, { emit }) {
    const imageUrl = ref(null);
    const onFileChange = (event: Event) => {
      const input = event.target as HTMLInputElement;
      if (input.files) {
        const file = input.files[0];
        imageUrl.value = URL.createObjectURL(file);
        emit('update', imageUrl.value);
      }
    };
    return {
      imageUrl,
      onFileChange
    };
  }
});
</script>
