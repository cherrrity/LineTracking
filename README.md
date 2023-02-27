# readme

### 22-1 자동차공학개론(Automotve Engineering)

---

최종성적 : A+

아키텍쳐 : 

![스크린샷 2023-02-27 22.25.10.png](readme%20ba9fd4dc7a22432ead58e89c51edae18/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-02-27_22.25.10.png)

![스크린샷 2023-02-27 22.25.21.png](readme%20ba9fd4dc7a22432ead58e89c51edae18/%25E1%2584%2589%25E1%2585%25B3%25E1%2584%258F%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25B5%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A3%25E1%2586%25BA_2023-02-27_22.25.21.png)

발표 영상 : 

[https://youtu.be/LA1jXglomyg](https://youtu.be/LA1jXglomyg)

시연 영상 :  

[https://youtu.be/VCtosd1FYDw](https://youtu.be/VCtosd1FYDw)

---

### 환경구성

```dart
sudo apt-get update
sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8- dev liblapack-dev libblas-dev gfortran
sudo pip3 install -U pip testresources setuptools==49.6.0
sudo pip3 install -U numpy==1.19.4 future==0.18.2 mock==3.0.5 h5py==2.10.0 keras_preprocessing==1.1.1 keras_applications==1.0.8 gast==0.2.2 futures protobuf pybind11

**sudo pip3 install --pre --extra-index-url** https://developer.download.nvidia.com/compute/redist/jp/v45 tensorflow
```

### 코드실행

```dart
python3 auto_control.py log_file_name [log file name]
```