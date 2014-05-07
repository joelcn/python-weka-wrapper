# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# dataset.py
# Copyright (C) 2014 Fracpete (fracpete at gmail dot com)

import matplotlib.pyplot as plt
from weka.core.classes import Random
from weka.core.dataset import Instances


def create_subsample(data, percent, seed=1):
    """
    Generates a subsample of the dataset.
    :param data: the data to create the subsample from
    :type data: Instances
    :param percent: the percentage (0-100)
    :type percent: float
    :param seed: the seed value to use
    :type seed: int
    """
    if percent <= 0 or percent >= 100:
        return data
    data = Instances.copy_instances(data)
    data.randomize(Random(seed))
    data = Instances.copy_instances(data, 0, round(data.num_instances() * percent / 100.0))
    return data


def scatter_plot(data, index_x, index_y, percent=100.0, seed=1, size=50, outfile=None, wait=True):
    """
    Plots two attributes against each other.
    TODO: click events http://matplotlib.org/examples/event_handling/data_browser.html
    :param data: the dataset
    :type data: Instances
    :param index_x: the 0-based index of the attribute on the x axis
    :type index_x: int
    :param index_y: the 0-based index of the attribute on the y axis
    :type index_y: int
    :param percent: the percentage of the dataset to use for plotting
    :type percent: float
    :param seed: the seed value to use for subsampling
    :type seed: int
    :param size: the size of the circles in point
    :type size: int
    :param outfile: the (optional) file to save the generated plot to. The extension determines the file format.
    :type outfile: str
    :param wait: whether to wait for the user to close the plot
    :type wait: bool
    """
    # create subsample
    data = create_subsample(data, percent=percent, seed=seed)

    # collect data
    x = []
    y = []
    if data.get_class_index() == -1:
        c = None
    else:
        c = []
    for i in xrange(data.num_instances()):
        inst = data.get_instance(i)
        x.append(inst.get_value(index_x))
        y.append(inst.get_value(index_y))
        if not c is None:
            c.append(inst.get_value(inst.get_class_index()))

    # plot data
    fig, ax = plt.subplots()
    if c is None:
        ax.scatter(x, y, s=size, alpha=0.5)
    else:
        ax.scatter(x, y, c=c, s=size, alpha=0.5)
    ax.set_xlabel(data.get_attribute(index_x).get_name())
    ax.set_ylabel(data.get_attribute(index_y).get_name())
    ax.set_title("Attribute scatter plot")
    ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c="0.3")
    ax.grid(True)
    fig.canvas.set_window_title(data.get_relationname())
    plt.draw()
    if not outfile is None:
        plt.savefig(outfile)
    if wait:
        plt.show()


def matrix_plot(data, percent=100.0, seed=1, size=10, outfile=None, wait=True):
    """
    Plots all attributes against each other.
    TODO: click events http://matplotlib.org/examples/event_handling/data_browser.html
    :param data: the dataset
    :type data: Instances
    :param percent: the percentage of the dataset to use for plotting
    :type percent: float
    :param seed: the seed value to use for subsampling
    :type seed: int
    :param size: the size of the circles in point
    :type size: int
    :param outfile: the (optional) file to save the generated plot to. The extension determines the file format.
    :type outfile: str
    :param wait: whether to wait for the user to close the plot
    :type wait: bool
    """
    # create subsample
    data = create_subsample(data, percent=percent, seed=seed)

    fig = plt.figure()

    if data.get_class_index() == -1:
        c = None
    else:
        c = []
        for i in xrange(data.num_instances()):
            inst = data.get_instance(i)
            c.append(inst.get_value(inst.get_class_index()))

    for index_x in xrange(data.num_attributes()):
        x = []
        for i in xrange(data.num_instances()):
            inst = data.get_instance(i)
            x.append(inst.get_value(index_x))
        for index_y in xrange(data.num_attributes()):
            y = []
            for i in xrange(data.num_instances()):
                inst = data.get_instance(i)
                y.append(inst.get_value(index_y))
            ax = fig.add_subplot(data.num_attributes(), data.num_attributes(), index_x * data.num_attributes() + index_y + 1)
            if c is None:
                ax.scatter(x, y, s=size, alpha=0.5)
            else:
                ax.scatter(x, y, c=c, s=size, alpha=0.5)
            ax.set_xlabel(data.get_attribute(index_x).get_name())
            ax.set_ylabel(data.get_attribute(index_y).get_name())
            ax.get_yaxis().set_ticklabels([])
            ax.get_xaxis().set_ticklabels([])
            ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c="0.3")
            ax.grid(True)
    fig.canvas.set_window_title(data.get_relationname())
    plt.draw()
    if not outfile is None:
        plt.savefig(outfile)
    if wait:
        plt.show()
