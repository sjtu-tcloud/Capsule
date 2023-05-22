#include <stdio.h>
#include <fcntl.h>
#include <errno.h>
#include <string.h>
#include <sys/ioctl.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/stat.h>

#include <capsule.h>
#include "utils.inc"

struct system_config sys_config = {
    .platform = {
        .pci_mmconfig_base = 0xb0000000,
        .pci_mmconfig_end_bus = 0xff,
        .vtd_interrupt_limit = 256,
        .iommu_unit.base = 0xfed90000,
        .iommu_unit.size = 0x1000,
        .pm_timer_address = 0x608,
    },
}

struct {
    struct cell_config cell;
    char cpu[4];
    struct memory_region mems[3];
    struct capsule_pio pios[5];
    struct capsule_data datas[4];
    struct cappsule_irqchip irqchips[1];
} __attribute__((packed)) config = {
    .cell = {
        .name = "linux-demo",
        .num_cpus = ARRAY_SIZE(config.cpus),
        .cpus = config.cpus,
        .mems = config.mems,
        .num_pios = ARRAY_SIZE(config.pios),
        .pios = config.pios,
        .num_datas = ARRAY_SIZE(config.datas),
        .datas = config.datas,
        .num_irqchips = ARRAY_SIZE(config.irqchips),
        .irqchips = config.irqchips,
    },
    .cpus = {
        5, 6, 7, 8,
    },
    .mems = {
        {
            .phys_start = 0x3a000000,
            .virt_start = 0,
            .size = 0x00100000,
        }, 
        {
            .phys_start = 0x3a100000,
            .virt_start = 0x100000,
            .size = 0x00001000,
        },
        {
            .phys_start = 0x3a200000,
            .virt_start = 0x00200000,
            .size = 0x5000000,
        },
    },
    .pios = {
        {
            base = 0x60,
            length = 8, 
        },
        {
            base = 0x40,
            length = 4, 
        },
        {
            base = 0x2f8,
            length = 8, 
        },
        {
            base = 0x3f8,
            length = 8, 
        },
        {
            base = 0xe010,
            length = 8, 
        },
    },
    .datas = {
        {
            .virt_start = 0,
        },
        {
            .virt_start = 0x1000,
        },
        {
            .virt_start = 0xffc600,
        },
        {
            .virt_start = 0x3dca000,
        },
    },
    .irqchips = {
        {
            .address = 0xfec00000,
            .id = 0xff00,
            .pin_bitmap = {
                (1 << 3) | (1 << 4),
            }
        }
    }
}

int main(int argc, char **argv) 
{
    int ret;
    int fd;
    char *asm_path = NULL;

    fd = open("/dev/capsule", O_RDWR);
    if (fd < 0) {
        printf("open fail: %s\n", strerror(errno));
        return -1;
    }

    config.cell.name_len = strlen(config.cell.name) + 1;
    asm_path = get_bin_path(argv[0], "/bins/linux-loader.bin");
    get_capsule_data(asm_path, &config.cell.datas[0]);
    asm_path = get_bin_path(argv[0], "/bins/boot_param.bin");
    get_capsule_data(asm_path, &config.cell.datas[1]);
    asm_path = get_bin_path(argv[0], "/bins/linuz.bin");
    get_capsule_data(asm_path, &config.cell.datas[2]);
    asm_path = get_bin_path(argv[0], "/bins/rt-tests.cpio");
    get_capsule_data(asm_path, &config.cell.datas[3]);
    free(asm_path);

    if ((ret = ioctl(fd, PARTITION_ENABLE, &sys_config)) < 0) {
        printf("ioctl PARTITION_ENABLE fail: %s\n", strerror(errno));
        goto err;
    }

    if ((ret = ioctl(fd, CELL_CREATE, &config.cell)) < 0) {
        printf("ioctl CELL_CREATE fail: %s\n", strerror(errno));
        goto err;
    }

    printf("========= CELL_CREATE success, waiting 10s...\n");
    sleep(10);

    if ((ret = ioctl(fd, CELL_DESTROY, 1)) < 0) {
        printf("ioctl CELL_DESTROY fail: %s\n", strerror(errno));
        goto err;
    }

    printf("========= CELL_CREATE success\n");
    ioctl(fd, PARTITION_DISABLE);

err:
    close(fd);
    free(config.cell.datas[0].data);
    free(config.cell.datas[1].data);
    free(config.cell.datas[2].data);
    return ret;
}