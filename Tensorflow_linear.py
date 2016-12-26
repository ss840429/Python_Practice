#!/usr/bin/python3
# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

x_data = np.random.rand(1000)
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = x_data*0.4 + 0.7 + noise

W = tf.Variable(tf.zeros([1]))
b = tf.Variable(tf.zeros([1]))
output = W*x_data + b

loss = tf.reduce_mean(tf.square(output - y_data))
train = tf.train.GradientDescentOptimizer(0.5).minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for step in range(201):
        sess.run(train)
        if step % 20 == 0:
            print(step, sess.run(W), sess.run(b))