# 三幻Spine动态立绘还原解决方案

本项目提供了一套完整的三幻Spine动态立绘还原解决方案，
帮助您从游戏文件中还原美术资源并重建动态立绘。

## 前置条件

在开始使用本工具之前，请确保满足以下条件：

### 环境要求
- **Python 3**：需要安装Python 3.x版本
  ```bash
  # 检查Python版本
  python --version
  # 或者
  python3 --version
  ```

### 必读文档
- **[AboutArtsResource.md](./AboutArtsResource.md)**：详细说明了如何从游戏中提取原始美术资源
  - 包含完整的资源提取教程
  - 支持安卓设备和模拟器
  - 涵盖文件传输和目录设置

### 重要提醒
- 请先按照 [AboutArtsResource.md](./AboutArtsResource.md) 的指引提取游戏美术资源
- 确保已获得包含 `miniRes` 目录的完整资源文件


## 功能特性

- 🔧 **文件扩展名恢复** - 自动识别并恢复文件的真实扩展名
- 📁 **智能文件分类** - 按文件类型自动整理到对应目录
- 🖼️ **图片尺寸重命名** - 根据图片尺寸自动重命名PNG文件
- 🔍 **资源内容搜索** - 快速定位atlas和skel文件中的特定内容
- 🎮 **完整工作流** - 从原始文件到Spine动态立绘的完整解决方案

## 快速开始

### 第一步：恢复文件扩展名

使用 `restore_file_ext.py` 来识别和恢复文件的真实扩展名：

```bash
python restore_file_ext.py <目录路径>
```

**示例：**
```bash
python restore_file_ext.py ./miniRes
```

### 第二步：按扩展名分类文件

使用 `move_files_by_ext_to_target_dir.py` 将不同类型的文件移动到对应目录：

```bash
python move_files_by_ext_to_target_dir.py <源目录> <扩展名> <目标目录名>
```

**示例：**

```bash
# 将atlas文件移动到atlas目录
python move_files_by_ext_to_target_dir.py ./miniRes .atlas ../atlas

# 将skel文件移动到skels目录
python move_files_by_ext_to_target_dir.py ./miniRes .skel ../skels
```


**⚠️注意⚠️**
- 示例中没有将图片归类，原因：
   - 图片数量非常庞大，归类到一起将很难找到需要的立绘
- 脚本的目标目录是基于源目录（即工作目录miniRes）
- `../atlas` 和 `../skels` 中的`..`表示上一层目录
- 归类不要存放在工作目录（即miniRes），以免造成重复处理甚至发生死循环

### 第三步：重命名PNG文件

使用 `rename_png_files.py` 根据图片尺寸重命名PNG文件：

```bash
python rename_png_files.py <目录路径>
```

**示例：**
```bash
python rename_png_files.py ./miniRes
```

完成以上三步后，您将获得完整的美术资源（PNG、SKEL和ATLAS文件）。

## Spine动态立绘还原指南

### 步骤1：定位目标立绘

1. 在重命名好的图片中找到您需要的角色立绘碎片
2. 将图片移动到您的存储文件夹
3. 记录图片的尺寸（如：size_2017x1937.png，即图片尺寸为2017,1937）

**注意**
- 存储文件夹指的是您存放还原资源的目录，例如：`三幻资源提取/赤焰周瑜`。
- 存储文件夹***不建议**放置在miniRes目录（即工作目录）内，会降低后续查找其他立绘的准确性。

### 步骤2：查找对应的Atlas文件

使用 `search_atlas_content.py` 根据图片尺寸搜索对应的atlas文件：

```bash
python search_atlas_content.py <atlas目录> "宽度,高度"
```

**示例：**
```bash
python search_atlas_content.py ./atlas "2017,1937"
```

**注意事项：**
- 可能会出现多个搜索结果
- 打开对应的.atlas文件查看具体细节
- 寻找与角色相关的动画参数（如：sp孙策的"biaoqing_jiangdongzhizhi"【江东之志】）
- 确定正确的atlas文件后移动至存储文件夹

### 步骤3：查找对应的Skel文件

1. 以文本形式打开找到的.atlas文件
2. 寻找特殊的动画部位名称（如：`biaoqing_jiangdongzhizhi`、`biaoqing_yansu`）
3. 使用 `search_skel_content.py` 搜索对应的skel文件：

```bash
python search_skel_content.py <skel目录> "动画部位1" "动画部位2" ...
```

**示例：**
```bash
python search_skel_content.py ./skels "biaoqing_jiangdongzhizhi" "biaoqing_yansu"
```

**提示：** 可以检索多个动画部位以提高搜索准确度。

### 步骤4：文件整理和导入

1. **重命名骨骼图片：**
   - 骨骼图片重命名为 `skeleton.png`
   - 如有多张，按atlas文件中的描述命名。例如：

    ```
    skeleton.png
    size: 2017,1937
    skeleton1.png
    size: 300,169
    ```
    > 尺寸为2017,1937的图片重命名为：skeleton.png
    
    > 尺寸为300,169的图片重命名为：skeleton1.png

2. **命名其他文件：**
   - `.skel` 和 `.atlas` 文件可根据个人喜好命名
   - 建议使用有意义的名称便于识别

3. **导入Spine软件：**
   - 将整理好的文件导入支持Spine合成的软件
   - 推荐软件：Live2DViewerEx

## 工具说明

| 工具文件 | 功能描述 | 使用场景 |
|---------|---------|---------|
| `restore_file_ext.py` | 恢复文件扩展名 | 初始文件处理 |
| `move_files_by_ext_to_target_dir.py` | 按扩展名分类文件 | 文件整理 |
| `rename_png_files.py` | 按尺寸重命名PNG | 图片标准化 |
| `search_atlas_content.py` | 搜索atlas内容 | 定位动画资源 |
| `search_skel_content.py` | 搜索skel内容 | 匹配骨骼文件 |

## 常见问题

### Q: 搜索结果为空怎么办？
A: 请检查：
- 目录路径是否正确
- 搜索关键词是否准确
- 文件扩展名是否正确恢复

### Q: 如何提高搜索准确度？
A: 建议：
- 使用多个动画部位名称进行搜索
- 结合atlas文件内容验证
- 检查文件命名规则

### Q: 为什么atlas文件不支持多信息搜索？
A: 因为我们能获取到检索.atlas文件的唯一信息只有图片尺寸

### Q: 支持哪些Spine软件？
A: 本工具提取的资源格式标准，支持主流Spine软件：
- Live2DViewerEx
- 其他支持Spine格式的软件

## 注意事项

- 请确保有足够的学习动机使用本工具
- 建议在备份原始文件的情况下进行操作

通过以上方法，您就能成功找到并还原喜欢的角色动态立绘！

动态立绘可用作个人搜藏/桌面动态壁纸/桌宠。
