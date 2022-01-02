<template>
    <div class="uploader"
        @dragenter="OnDragEnter"
        @dragleave="OnDragLeave"
        @dragover.prevent
        @drop="onDrop"
        :class="{ dragging: isDragging }">
        
        <div class="upload-control" v-show="images.length"
             style="left: 50%; transform: translateX(-50%);">
            <label for="file">Select a file</label>
            <button @click="upload">Upload</button>
        </div>


        <div v-show="!images.length">
            <i class="fa fa-cloud-upload"></i>
            <p>拖动图片到此处</p>
            <div>或</div>
            <div class="file-input">
                <label for="file">选择图片</label>
                <input type="file" id="file" @change="onInputChange" multiple>
            </div>
        </div>

        <div class="images-preview" v-show="images.length">
            <div class="img-wrapper" v-for="(image, index) in images" :key="index">
                <img :src="image" :alt="`Image Uplaoder ${index}`">
                <div class="details">
                    <span class="name" v-text="files[index].name"></span>
                    <span class="size" v-text="getFileSize(files[index].size)"></span>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import Bus from '@/api/bus'
export default {
    data: () => ({
        isDragging: false,
        dragCount: 0,
        files: [],
        images: []
    }),
    methods: {
        OnDragEnter(e) {
            e.preventDefault();
            
            this.dragCount++;
            this.isDragging = true;

            return false;
        },
        OnDragLeave(e) {
            e.preventDefault();
            this.dragCount--;

            if (this.dragCount <= 0)
                this.isDragging = false;
        },
        onInputChange(e) {
            const files = e.target.files;

            Array.from(files).forEach(file => this.addImage(file));
        },
        onDrop(e) {
            e.preventDefault();
            e.stopPropagation();

            this.isDragging = false;

            const files = e.dataTransfer.files;

            Array.from(files).forEach(file => this.addImage(file));
        },
        addImage(file) {
            if (!file.type.match('image.*')) {
                this.$toastr.e(`${file.name} is not an image`);
                return;
            }

            this.files.push(file);

            // const img = new Image();
               const reader = new FileReader();

            reader.onload = (e) => this.images.push(e.target.result);

            reader.readAsDataURL(file);

        },
      deleteImage(file) {
            if (!file.type.match('image.*')) {
                this.$toastr.e(`${file.name} is not an image`);
                return;
            }

            this.files.pop(file)

            // const img = new Image();
            const reader = new FileReader();
            reader.onload = (e) => this.images.pop(e.target.result);

            reader.readAsDataURL(file);
            this.$message("成功删除图片")
        },
        getFileSize(size) {
            const fSExt = ['Bytes', 'KB', 'MB', 'GB'];
            let i = 0;
            
            while(size > 900) {
                size /= 1024;
                i++;
            }

            return `${(Math.round(size * 100) / 100)} ${fSExt[i]}`;
        },
        upload() {

            const formData = new FormData();
            let cnt = 0;
            
            this.files.forEach(file => {
                cnt = cnt+1;
                formData.append('file'+cnt, file, file.name);
            });
            formData.append('cnt', cnt);

            this.axios({method: 'post', url: '/main/upload',data: formData})
            .then(
              response => {
                if (response.data['code'] === 200) {
                   // this.$toastr.s('All images uplaoded successfully');
                  this.$message('上传成功')
                  this.images = [];
                  this.files = [];
                  Bus.$emit('filearr', response.data['filearr'])
                }
              })
          .catch(function (error) {
            console.log(error);
          })
        }
    }
}
</script>


<style lang="scss" scoped>
.uploader {
    background: #ccdeee;
    color: #fff;
    padding: 40px 15px;
    text-align: center;
    border-radius: 10px;
    border: 1px dashed #fff;
    font-size: 20px;
    position: relative;
  display: flex;
  justify-content: center;

    &.dragging {
        background: #fff;
        color: #ccdeee;
        border: 3px dashed #ccdeee;


        .file-input label {
            background: #ccdeee;
            color: #fff;
        }
    }

    i {
        font-size: 85px;
    }

    .file-input {
        margin: auto;
        height: 68px;
        position: relative;

        label,
        input {
            background: #fff;
            color: #ccdeee;
            position: absolute;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            top: 0;
            padding: 10px;
            border-radius: 4px;
            margin-top: 7px;
            cursor: pointer;
        }

        input {
            opacity: 0;
            z-index: -2;
        }
    }

    .images-preview {
        display: flex;
        flex-wrap: wrap;
        margin-top: 20px;

        .img-wrapper {
            width: 160px;
            display: flex;
            flex-direction: column;
            margin: 10px;
            height: 150px;
            justify-content: space-between;
            background: #fff;
            box-shadow: 5px 5px 20px #3e3737;

            img {
                max-height: 105px;
            }
        }

        .details {
            font-size: 12px;
            background: #fff;
            color: #000;
            display: flex;
            flex-direction: column;
            align-items: self-start;
            padding: 3px 6px;

            .name {
                overflow: hidden;
                height: 18px;
            }
        }
    }

    .upload-control {
        position: absolute;
        width: 100%;
        background: #fff;
        top: 0;
        left: 0;
        border-top-left-radius: 7px;
        border-top-right-radius: 7px;
        padding: 5px;
        padding-bottom: 5px;
        text-align: center;

        button, label {
            background: #2196F3;
            border: 2px solid #03A9F4;
            border-radius: 3px;
            color: #fff;
            font-size: 15px;
            cursor: pointer;
        }

        label {
            padding: 2px 5px;
            margin-right: 10px;
        }
    }
}
</style>