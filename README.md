# AutoTrain
## Features
Trains automaticly (look in the code)
## Important twerks for tensorflow in order to save all checkpoints
## 1 keep all checkpoints
* Found [here](https://github.com/tensorflow/models/issues/5076)
* Add ```keep_checkpoint_max=0``` like ```config = tf.estimator.RunConfig(model_dir=FLAGS.model_dir, keep_checkpoint_max=500)``` in model_main.py.
* Add ```max_to_keep= 10000``` (or large number) to model_lib.py like that in saver:
```py
saver = tf.train.Saver(
	variables_to_restore,
	keep_checkpoint_every_n_hours=keep_checkpoint_every_n_hours,
	max_to_keep=500)# <= added max_to_keep argument here
	
	
saver = tf.train.Saver(
	sharded=True,
	keep_checkpoint_every_n_hours=keep_checkpoint_every_n_hours,
	save_relative_paths=True,
	max_to_keep=500)# <= added max_to_keep argument here
  ```
  ## 2 keep checkpoint every n steps
  * link from [here](https://github.com/tensorflow/models/issues/5139#issuecomment-418963839)
  * Add ```save_checkpoints_steps=1000``` (or any other number) to ```config = tf.estimator.RunConfig(model_dir=FLAGS.model_dir, session_config=session_config, save_checkpoints_steps=1000, keep_checkpoint_max=None)``` in model_main.py
