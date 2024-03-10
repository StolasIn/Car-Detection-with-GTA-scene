1. 
prepare_dataset.py 為處理資料集的程式，但使用前必須先把 image folder 的檔名加上 2017
ex. val -> val2017, train -> train2017...

2.
yolox_x.py 是超參數設定

3.
需要建置環境請跟著以下指令操作
	1. cd path/to/YOLOX (YOLOX 的資料夾 Original 或是 SE)
	2. conda env create -f environment.yml
	3. conda activate VSTHW2
	4. pip uninstall setuptools
	5. pip install setuptools==65.0.0
	6. python3 setup.py develop

由於 YOLOX 的環境有些複雜，並不確定是否能 100% 重建，但目前以上指令可以在另一台機器上重建


4.
需要產生計算 AP 的資料，請使用位於不同 code 資料夾內部的 eval.sh
產生完的結果會放在 code 資料夾內的 detections 中，請注意

以下是範例
python tools/demo.py image -f exps/example/custom/yolox_x.py -c best_ckpt_normal.pth --path datasets/HW2_ObjectDetection_2023/test --device gpu --conf 0.01 --nms 0.65

需要注意以下的檔案位置是否都是正確的
-f : 擺放 exp 的位置 (如果找不到或是路徑有錯誤，可以使用檔案外的 yolox_x.py)
-c : 預訓練模型的 weight (內外都有放一份 best_ckpt_normal.pth 表示原本的 YOLOX, best_ckpt_SE.pth 表示有 SE 的版本)
--path : 擺放 test image 的位置 (預設是放 val2017 表示驗證資料集，如果需要修改可以改成測試資料集)
