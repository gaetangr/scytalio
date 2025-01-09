<template>
  <div class="toast toast-bottom toast-end">
    <div v-if="show" :class="['alert', `alert-${type}`]">
      <span>{{ text }}</span>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Toast',
    props: {
      show: {
        type: Boolean,
        default: false,
      },
      text: {
        type: String,
        default: 'Notification',
      },
      type: {
        type: String,
        default: 'success',
        validator: value => {
          return ['info', 'success', 'warning', 'error'].includes(value);
        },
      },
    },
  };
</script>
